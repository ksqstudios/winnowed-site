# winnowed-site

Marketing site for [Winnowed](https://winnowed.app), the subscription tracker designed around a quarterly review ritual.

## Structure

```
winnowed-site/
├── index.html              → winnowed.app/
├── styles.css              → shared stylesheet
├── privacy/index.html      → winnowed.app/privacy
├── support/index.html      → winnowed.app/support
└── images/
    ├── stack.png
    ├── review.png
    └── widget.png
```

Static HTML/CSS with no build step. Typography is Young Serif (display) and Libre Franklin (body) via Google Fonts. Colors pull from Winnowed's five-stage harvest palette, sage to burgundy. The home page opens on a review you can try: cut subscriptions blow away as chaff, kept ones add up to the Winnowed Number.

## Deploy (Cloudflare Pages)

Same pattern as the Minuted site:

1. Create a new GitHub repo named `winnowed-site` under `09kleinkd`.
2. `git init`, `git add .`, `git commit`, `git push`.
3. In Cloudflare, Workers & Pages → Create → Pages → Connect to Git → pick `winnowed-site`.
4. Build settings: leave everything blank. Output directory: `/`.
5. Deploy.
6. Custom domain: add `winnowed.app` and `www.winnowed.app`.

Every `git push` to `main` auto-deploys.

## Analytics

None. The site collects nothing, and the privacy policy says so.
