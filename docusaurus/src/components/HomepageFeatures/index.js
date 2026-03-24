import React from "react";

const FeatureList = [
    {
        title: "Intégration rapide",
        description: "Quickstart clair, exemples Python, structure prête pour les intégrateurs.",
    },
    {
        title: "SDK industriel",
        description: "Abstraction des transports RS-232 / RS-485 / Ethernet et logique capteur ISRA.",
    },
    {
        title: "Documentation FR/EN",
        description: "Expérience bilingue native pour les équipes locales et internationales.",
    },
];

function Feature({ title, description }) {
    return (
        <div className="col col--4">
            <div className="featureCard">
                <h3>{title}</h3>
                <p>{description}</p>
            </div>
        </div>
    );
}

export default function HomepageFeatures() {
    return (
        <section className="featuresSection">
            <div className="container">
                <div className="row">
                    {FeatureList.map((props, idx) => (
                        <Feature key={idx} {...props} />
                    ))}
                </div>
            </div>
        </section>
    );
}
