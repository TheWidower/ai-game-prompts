# MCP client templates

Replace YOU, paths, and ports. Absolute paths only. Do not mix stacks.

Client file locations are in `references/mcp-config.md`.

## Official Unity MCP (relay)

Windows

```json
{
  "mcpServers": {
    "unity-mcp": {
      "command": "C:/Users/YOU/.unity/relay/relay_win.exe",
      "args": ["--mcp"]
    }
  }
}
```

macOS Apple Silicon

```json
{
  "mcpServers": {
    "unity-mcp": {
      "command": "/Users/YOU/.unity/relay/relay_mac_arm64.app/Contents/MacOS/relay_mac_arm64",
      "args": ["--mcp"]
    }
  }
}
```

Several Editors

```json
"args": ["--mcp", "--project-path", "D:/MyUnityProject"]
```

Approve Pending Connection in Edit > Project Settings > AI > Unity MCP.

## Community Unity-MCP (AI Game Developer)

HTTP — port is SHA256(project path) in 20000–29999. Read it from the dashboard.

```json
{
  "mcpServers": {
    "ai-game-developer": {
      "type": "http",
      "url": "http://localhost:PORT"
    }
  }
}
```

## Official Unreal MCP (UE 5.8)

```json
{
  "mcpServers": {
    "unreal-mcp": {
      "type": "http",
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

No auth. Loopback only. Enable Auto Start or run `ModelContextProtocol.StartServer`.
Generate files with `ModelContextProtocol.GenerateClientConfig ClaudeCode`.

## Community ue-mcp

```json
{
  "mcpServers": {
    "ue-mcp": {
      "command": "npx",
      "args": ["ue-mcp", "C:/path/to/MyGame.uproject"]
    }
  }
}
```

Forward slashes on Windows. Bridge WS is `localhost:9877`.

## Godot AI

Do not use raw `http://127.0.0.1:8000/mcp`.
Use the Godot AI dock Configure button (stdio `godot-ai attach`).
If you must paste by hand, paste the command the dock shows.

## GDAI MCP

```json
{
  "mcpServers": {
    "gdai-mcp-server": {
      "command": "uv",
      "args": ["run", "PATH_FROM_DOCK"],
      "env": {
        "GDAI_MCP_SERVER_PORT": "3571",
        "GDAI_RUNTIME_SERVER_PORT": "3572"
      }
    }
  }
}
```

## First prompts after connect

```
Ping the plugin and list tool families.
```

```
In the current scene, create a cube named McpProbe at the origin, then take a screenshot.
```
