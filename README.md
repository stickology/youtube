# youtube

YouTube channel workspace with the [youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) pack (MIT) installed project-local in `.claude/skills/`.

Commands: `/yt-script`, `/yt-package`, `/yt-edit`, `/yt-comment`, `/yt-plan`, `/yt-viral`, `/yt-retention`, `/yt-shorts`, `/yt-seo`, `/yt-chapters`, `/yt-audit`.

## Voice profile

Every skill reads `~/.claude/youtube/voice.md`. Fill in `youtube/voice.md` here (or ask Claude to write it from three of your videos), then copy it into place at the start of a session:

```bash
mkdir -p ~/.claude/youtube && cp youtube/voice.md ~/.claude/youtube/voice.md
```
