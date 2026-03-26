# Docusaurus - ISRA Sensor SDK

## Lancer en local

```bash
npm install
npm run start
```

## Emplacement des assets branding (PNG)

Placez votre unique fichier ici :

- `static/img/logo.png` (utilisé à la fois pour le logo navbar et le favicon)

La configuration est déjà branchée dans `docusaurus.config.js`.

## Déploiement GitHub Pages

Configuration déjà prête pour ton repo :

- `url: "https://yannis-isra.github.io"`
- `baseUrl: "/isra-sensor-sdk/"`
- `organizationName: "Yannis-ISRA"`

Il ne te reste qu'à :

1. Push sur GitHub
2. `Settings` → `Pages` → `Source = GitHub Actions`
3. Vérifier le workflow `Deploy Docusaurus to GitHub Pages`

URL finale : `https://yannis-isra.github.io/isra-sensor-sdk/`
