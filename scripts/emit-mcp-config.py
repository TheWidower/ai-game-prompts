#!/usr/bin/env python3
"""Emit a copy-paste MCP client config for a known game-engine stack."""

from __future__ import annotations

import argparse
import json
import sys

STACKS = ("unity-official", "unity-community", "godot-ai", "gdai", "unreal-official", "ue-mcp")
CLIENTS = ("claude-code", "claude-desktop", "cursor", "vscode", "codex")
OSES = ("windows", "mac-arm", "mac-intel", "linux")

FILE_FOR_CLIENT = {
    "claude-code": "project .mcp.json  (or ~/.claude.json)",
    "claude-desktop": {
        "windows": r"%APPDATA%\Claude\claude_desktop_config.json",
        "mac-arm": "~/Library/Application Support/Claude/claude_desktop_config.json",
        "mac-intel": "~/Library/Application Support/Claude/claude_desktop_config.json",
        "linux": "~/.config/Claude/claude_desktop_config.json",
    },
    "cursor": "project .cursor/mcp.json",
    "vscode": "project .vscode/mcp.json",
    "codex": "project .codex/config.toml or ~/.codex/config.toml",
}

UNITY_RELAY = {
    "windows": "C:/Users/YOU/.unity/relay/relay_win.exe",
    "mac-arm": "/Users/YOU/.unity/relay/relay_mac_arm64.app/Contents/MacOS/relay_mac_arm64",
    "mac-intel": "/Users/YOU/.unity/relay/relay_mac_x64.app/Contents/MacOS/relay_mac_x64",
    "linux": "/home/YOU/.unity/relay/relay_linux",
}


def wrap(name: str, body: dict) -> dict:
    return {"mcpServers": {name: body}}


def emit(stack: str, client: str, os_name: str, project: str, port: str) -> tuple[str, object, list[str]]:
    notes: list[str] = []
    dest = FILE_FOR_CLIENT[client]
    if isinstance(dest, dict):
        dest = dest[os_name]

    if stack == "unity-official":
        body = {"command": UNITY_RELAY[os_name], "args": ["--mcp"]}
        if project:
            body["args"] += ["--project-path", project]
        notes += [
            "Edit > Project Settings > AI > Unity MCP — Bridge must be Running.",
            "Accept Pending Connection on first connect.",
            "Use absolute paths. Do not leave YOU unreplaced.",
        ]
        return dest, wrap("unity-mcp", body), notes

    if stack == "unity-community":
        p = port or "PORT"
        notes += [
            "Port is SHA256(lowercase project dir) mapped to 20000-29999.",
            "Read the live port from Window > AI Game Developer. Do not guess.",
            "This is NOT the official Unity relay.",
        ]
        return dest, wrap("ai-game-developer", {"type": "http", "url": f"http://localhost:{p}"}), notes

    if stack == "godot-ai":
        notes += [
            "Do not point the client at http://127.0.0.1:8000/mcp.",
            "Use the Godot AI dock Configure button (godot-ai attach over stdio).",
            "Addon path must be addons/godot_ai/plugin.cfg.",
        ]
        body = {
            "command": "godot-ai",
            "args": ["attach"],
            "_comment": "Replace this block with the exact command the Godot AI dock prints.",
        }
        return dest, wrap("godot-ai", body), notes

    if stack == "gdai":
        notes += [
            "Mirror ports from gdai_mcp_project_config.json.",
            "Defaults are 3571 (MCP) and 3572 (runtime).",
        ]
        body = {
            "command": "uv",
            "args": ["run", "PATH_FROM_DOCK"],
            "env": {
                "GDAI_MCP_SERVER_PORT": port or "3571",
                "GDAI_RUNTIME_SERVER_PORT": "3572",
            },
        }
        return dest, wrap("gdai-mcp-server", body), notes

    if stack == "unreal-official":
        p = port or "8000"
        notes += [
            "Editor Preferences > Model Context Protocol. Auto Start or ModelContextProtocol.StartServer.",
            "No auth. Loopback only. Do not expose this URL.",
            "Generate files with ModelContextProtocol.GenerateClientConfig.",
        ]
        return dest, wrap("unreal-mcp", {"type": "http", "url": f"http://127.0.0.1:{p}/mcp"}), notes

    if stack == "ue-mcp":
        uproject = project or "C:/path/to/MyGame.uproject"
        notes += [
            "Run npx ue-mcp init once. Bridge listens on ws://localhost:9877.",
            "Use forward slashes in the uproject path.",
            "This is NOT official Unreal MCP on port 8000.",
        ]
        return dest, wrap("ue-mcp", {"command": "npx", "args": ["ue-mcp", uproject]}), notes

    raise SystemExit(f"unknown stack: {stack}")


def as_toml(name: str, body: dict) -> str:
    lines = [f"[mcp_servers.{name}]"]
    if body.get("type") == "http" or "url" in body:
        lines.append("type = \"http\"")
        lines.append(f"url = \"{body['url']}\"")
        lines.append("enabled = true")
        return "\n".join(lines) + "\n"
    lines.append(f"command = \"{body['command']}\"")
    args = body.get("args") or []
    inner = ", ".join(json.dumps(a) for a in args)
    lines.append(f"args = [{inner}]")
    if project_cwd := None:
        lines.append(f"cwd = \"{project_cwd}\"")
    lines.append("enabled = true")
    env = body.get("env")
    if env:
        lines.append("")
        lines.append(f"[mcp_servers.{name}.env]")
        for k, v in env.items():
            lines.append(f"{k} = \"{v}\"")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--stack", required=True, choices=STACKS)
    p.add_argument("--client", required=True, choices=CLIENTS)
    p.add_argument("--os", required=True, dest="os_name", choices=OSES)
    p.add_argument("--project", default="", help="Unity project dir, or Unreal .uproject path")
    p.add_argument("--port", default="", help="Override port when the stack uses HTTP")
    args = p.parse_args(argv)

    dest, payload, notes = emit(args.stack, args.client, args.os_name, args.project, args.port)
    print(f"# write to: {dest}")
    print(f"# stack: {args.stack}  client: {args.client}  os: {args.os_name}")
    for n in notes:
        print(f"# note: {n}")
    print()
    if args.client == "codex":
        name, body = next(iter(payload["mcpServers"].items()))
        print(as_toml(name, body), end="")
    else:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
