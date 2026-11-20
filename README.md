# youtube

YouTube channel workspace with two skill packs installed project-local in `.claude/skills/`:

- [youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) (MIT): the `/yt-*` commands
- [claude-youtube](https://github.com/AgriciDaniel/claude-youtube) (MIT): the `/youtube` command, including `/youtube thumbnail`

`.mcp.json` registers the NanoBanana MCP server for Gemini thumbnail generation. The API key is not stored in the repo; it is read from the `GEMINI_API_KEY` environment variable, or injected by a network secret for `generativelanguage.googleapis.com` (header `x-goog-api-key`).

Commands: `/yt-script`, `/yt-package`, `/yt-edit`, `/yt-comment`, `/yt-plan`, `/yt-viral`, `/yt-retention`, `/yt-shorts`, `/yt-seo`, `/yt-chapters`, `/yt-audit`.

## Voice profile

Every skill reads `~/.claude/youtube/voice.md`. Fill in `youtube/voice.md` here (or ask Claude to write it from three of your videos), then copy it into place at the start of a session:

```bash
mkdir -p ~/.claude/youtube && cp youtube/voice.md ~/.claude/youtube/voice.md
```
