import React from "react";
import Layout from "@theme/Layout";
import Link from "@docusaurus/Link";
import HomepageFeatures from "../components/HomepageFeatures";

export default function Home() {
    return (
        <Layout title="ISRA Sensor SDK" description="Documentation industrielle RFID UHF">
            <header className="hero hero--primary israHero">
                <div className="container">
                    <h1 className="hero__title">ISRA Sensor SDK</h1>
                    <p className="hero__subtitle">
                        Documentation d’intégration RFID UHF pour l’industrie (FR/EN)
                    </p>
                    <div className="heroCta">
                        <Link className="button button--secondary button--lg" to="/docs/quickstart">
                            🚀 Démarrer
                        </Link>
                        <Link className="button button--outline button--lg" to="/docs/integration-guide">
                            📘 Guide d’intégration
                        </Link>
                    </div>
                </div>
            </header>
            <main>
                <HomepageFeatures />
            </main>
        </Layout>
    );
}
