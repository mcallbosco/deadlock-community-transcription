# Deadlock Community Localizations

Community-contributed localization files for the Deadlock voiceline viewer.

## Structure

Each localization lives in its own folder under `localizations/`:

```
localizations/
  <language>/
    <original_vdf_filename>.vdf    # VDF file, using the game's original filename with a .vdf extension
    metadata.json                  # Metadata describing the localization
```

- `<language>` must be **lowercase**, use **underscores** instead of spaces, and contain only `a-z`, `0-9`, and `_`. The folder name must match the `language` field inside `metadata.json`.
- Keep the **original base filename as shipped with the game** (for example, `citadel_generated_vo_russian`) and use a `.vdf` extension.

A starter template is available at [`localizations/_template/`](localizations/_template/). Folders whose name starts with `_` are ignored by validation.

## `metadata.json` format

All fields are required.

```json
{
  "language": "russian_fan",
  "friendly_name": "Russian (Fan)",
  "native_name": "Русский (Фан)",
  "country_code": "RU",
  "flag_emoji": "🇷🇺",
  "tooltip_text": "Fan translation by Торфусняк",
  "credits": [
    {
      "name": "Telegram",
      "link": "https://t.me/tofamode"
    },
    {
      "name": "YouTube",
      "link": "https://www.youtube.com/@Torfusdeadlock"
    },
    {
      "name": "Discord: yukinnon",
      "link": null
    }
  ]
}
```

### Field reference

| Field | Type | Description |
|---|---|---|
| `language` | string | Identifier. Lowercase letters, digits, and underscores only. Must match the folder name. |
| `friendly_name` | string | English-facing display name (e.g. `"Russian (Fan)"`). |
| `native_name` | string | Display name written in the native script (e.g. `"Русский (Фан)"`). |
| `country_code` | string | ISO 3166-1 alpha-2 country code, uppercase (e.g. `"RU"`). |
| `flag_emoji` | string | Flag emoji for the language (e.g. `"🇷🇺"`). |
| `tooltip_text` | string | Short tooltip shown in the UI. |
| `credits` | array | At least one credit entry. See below. |

### Credits

Each entry in `credits` is an object with:

- `name` — display label (e.g. `"Telegram"`, `"Discord: yukinnon"`).
- `link` — URL string, or `null` for plain-text entries (used when there is no clickable link, e.g. a raw Discord handle).

The JSON Schema for `metadata.json` lives at [`schema/metadata.schema.json`](schema/metadata.schema.json).

## Contributing a localization

1. Fork this repo.
2. Create `localizations/<language>/`.
3. Add the original VDF file from the game and a `metadata.json` that matches the format above.
4. Open a pull request. CI will validate the folder layout, `metadata.json` contents, and that the VDF file is present.

### Requesting a new language or getting help

**DM `@mcall` on Discord** to request a language, ask about the format, or get help preparing a contribution.
