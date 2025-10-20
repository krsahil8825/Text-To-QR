# Contributing to Text To QR

Thanks for your interest in contributing! We welcome improvements of all sizes. This project participates in Hacktoberfest, so feel free to submit PRs that improve docs, code quality, accessibility, or features.

## Getting Started

1. Fork the repo and clone your fork
2. Create a new branch from `main`
3. Set up the project:
   - Create and activate a virtual environment (optional)
   - Install dependencies: `pip install -r requirements.txt`
   - Create a `.env` file (see `.env.example`)
   - Run the app: `python app.py`

## Development

- The main endpoint is `/` (GET/POST). POST expects a form field named `data`.
- Additional pages: `/about`, `/contact`.
- Static assets live in `static/`, templates in `templates/`.

## Code Style

- Keep code readable and type-hinted where helpful
- Avoid broad try/except; handle errors meaningfully
- Keep indentation/style consistent with existing files

## Submitting Changes

1. Format and lint your changes locally if possible
2. Keep commits focused and messages clear
3. Open a Pull Request with a concise description of:
   - What changed
   - Why it changed
   - Any screenshots for UI changes

## Good First Issues / Ideas

- Improve form validation and UX
- Add dark mode or better responsive styles
- Add a preview of the QR image before download
- Enhance README with screenshots/GIF
- Add unit tests for `generate_qr_code`

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
