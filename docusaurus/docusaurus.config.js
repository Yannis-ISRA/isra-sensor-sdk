// @ts-check

const config = {
    title: "ISRA Sensor SDK",
    tagline: "Documentation d'intégration industrielle RFID UHF",
    favicon: "img/logo.png",

    url: "https://yannis-isra.github.io",
    baseUrl: "/isra-sensor-sdk/",

    organizationName: "Yannis-ISRA",
    projectName: "isra-sensor-sdk",
    deploymentBranch: "gh-pages",
    trailingSlash: false,

    onBrokenLinks: "throw",
    onBrokenMarkdownLinks: "warn",

    i18n: {
        defaultLocale: "fr",
        locales: ["fr", "en"],
        localeConfigs: {
            fr: { label: "Français" },
            en: { label: "English" },
        },
    },

    presets: [
        [
            "classic",
            {
                docs: {
                    sidebarPath: "./sidebars.js",
                    routeBasePath: "/",
                    editUrl: "https://github.com/Yannis-ISRA/isra-sensor-sdk/tree/main/sdk_portal/docusaurus/",
                },
                blog: false,
                theme: {
                    customCss: "./src/css/custom.css",
                },
            },
        ],
    ],

    themeConfig: {
        colorMode: {
            respectPrefersColorScheme: true,
        },
        navbar: {
            title: "ISRA SDK",
            logo: {
                alt: "ISRA Logo",
                src: "img/logo.png",
            },
            items: [
                {
                    type: "docSidebar",
                    sidebarId: "tutorialSidebar",
                    position: "left",
                    label: "Documentation",
                },
                {
                    href: "https://github.com/Yannis-ISRA/isra-sensor-sdk",
                    label: "GitHub",
                    position: "right",
                },
                {
                    type: "localeDropdown",
                    position: "right",
                },
            ],
        },
        footer: {
            style: "dark",
            copyright: `© ${new Date().getFullYear()} ISRA CARDS - ISRA Sensor SDK`,
        },
        prism: {
            additionalLanguages: ["bash", "powershell", "python"],
        },
    },
};

module.exports = config;
