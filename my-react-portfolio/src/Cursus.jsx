import React, { useState, useEffect } from 'react';
import './Cursus.css'
import githubLogo from './assets/contact/github.png'
import etudeLogo from './assets/img/etudeW.png'
import devLogo from './assets/img/terminalW.png'
import proLogo from './assets/img/pro.png'


function Cursus(){
    return (
        <section id="parcours">
            <div className="Bloc-content">
                <h1>Mon <span id='Colored'>parcours</span></h1>
                <p>J'ai suivi un parcours académique atypique en choisissant un baccalauréat général avec les spécialités NSI, LLCER Anglais et SES.</p>
                
                <div className="parcour-history">
                    <div className="gradiation-bar"></div>
                    <div className="box-content-column" id="history-container">
        
                        <div className="box-content-row" id='period-box'>
                            <div className="period-circle" id='MDS'>
                                <img src={etudeLogo} alt="Test" />
                            </div>
                            <div className="period-content" id='MDS-content'>
                                <h2>MBA Développeur Full-Stack</h2>
                                <h3>MyDigitalSchool</h3>
                                <h4>Oct 2025 - Actuellement</h4>
                                <h4>Montpellier, 34080</h4>
                                <p>Formation niveau 7 (BAC+5) en développement web full-stack avancé.</p>
                                <div className="box-content-row" id="skills-list">
                                    <li>React</li>
                                    <li>Angular</li>
                                    <li>Node.js</li>
                                    <li>Docker</li>
                                    <li>Gestion de Projet</li>
                                    <li>Python</li>
                                    <li>Java</li>
                                    <li>Etc...</li>
                                </div>
                            </div>
                        </div>

                        <div className="box-content-row" id='period-box'>
                            <div className="period-circle" id='NASDY'>
                                <img src={devLogo} alt="Test" />
                            </div>
                            <div className="period-content" id='NASDY-content'>
                                <h2>Stage de développement Web</h2>
                                <h3>NASDY</h3>
                                <h4>Juin 2024 - Juillet 2024</h4>
                                <h4>FDF - Martinique</h4>
                                <p>Stage d'un mois à NASDY, où j'ai pu acquérir de nouvelles compétences. Notamment avec l'apprentissage de l'ERP Odoo.</p>
                                <div className="box-content-row" id="skills-list">
                                    <li>Odoo</li>
                                    <li>Odoo.sh</li>
                                    <li>Création de Site</li>
                                    <li>Base de Données</li>
                                    <li>Migration de Site</li>
                                </div>
                            </div>
                        </div>

                        <div className="box-content-row" id='period-box'>
                            <div className="period-circle" id='ISP2'>
                                <img src={proLogo} alt="Test" />
                            </div>
                            <div className="period-content" id='ISP2-content'>
                                <h2>Promotion au statut de directeur de l'ISP</h2>
                                <h3>ISP (ICEA)</h3>
                                <h4>Février 2024 - Octobre 2024</h4>
                                <h4>FDF - Martinique</h4>
                                <p>J'ai par la suite été promu en tant que directeur, où j'ai dû gerer davantages d'aspects administratifs de l'entreprise tout en restant un membre de l'équipe exécutive qui participe aux missions. </p>
                                <div className="box-content-row" id="skills-list">
                                    <li>Management des équipes</li>
                                    <li>Responsabilité des missions</li>
                                    <li>Réunion</li>
                                    <li>Gestion des relation Clients</li>
                                    <li>Rapport de missions</li>
                                    <li>Rédaction de mails</li>
                                </div>
                            </div>
                        </div>

                        <div className="box-content-row" id='period-box'>
                            <div className="period-circle" id='ISP'>
                                <img src={proLogo} alt="Test" />
                            </div>
                            <div className="period-content" id='ISP-content'>
                                <h2>Création d'une junior entreprise (ISP)</h2>
                                <h3>ISP (ICEA)</h3>
                                <h4>Sept 2023 - Février 2024</h4>
                                <h4>FDF - Martinique</h4>
                                <p>En deuxième année de LSDN, nous avons mené un projet de classe consistant à créer notre propre entreprise.
                                Nous avons donc créer l'ICEA School Partner (ISP), une junior entreprise d'aide à la numérisation aux professionels et particuliers. 
                                J'ai débuté cette aventure en tant que Responsable Marketing.</p>
                                <div className="box-content-row" id="skills-list">
                                    <li>Création de documents administratifs</li>
                                    <li>Réunion de votes</li>
                                    <li>Crétion de logos</li>
                                    <li>Création de Flyers</li>
                                    <li>Gestion des réseaux sociaux</li>
                                </div>
                            </div>
                        </div>

                        <div className="box-content-row" id='period-box'>
                            <div className="period-circle" id='LSDN'>
                                <img src={proLogo} alt="Test" />
                            </div>
                            <div className="period-content" id='LSDN-content'>
                                <h2>Licence Sciences du Numérique</h2>
                                <h3>ICEA</h3>
                                <h4>Sept 2022 - Juin 2025</h4>
                                <h4>FDF - Martinique</h4>
                                <p>Formation niveau 6 (BAC+3) dans plusieurs aspect du numérique.</p>
                                <div className="box-content-row" id="skills-list">
                                    <li>Python</li>
                                    <li>HTML</li>
                                    <li>CSS</li>
                                    <li>JavaScript</li>
                                    <li>SQL</li>
                                    <li>PHP</li>
                                    <li>Java</li>
                                    <li>C</li>
                                    <li>C++</li>
                                    <li>C#</li>
                                    <li>Bash</li>
                                    <li>Réseaux et sécurité</li>
                                    <li>Système d'exploitation</li>
                                    <li>Gestion de Projets</li>
                                    <li>Anglais</li>
                                    <li>UE5</li>
                                    <li>Unity</li>
                                    <li>VR</li>
                                </div>
                            </div>
                        </div>

                        <div className="box-content-row" id='period-box'>
                            <div className="period-circle" id='Bac'>
                                <img src={etudeLogo} alt="Test" />
                            </div>
                            <div className="period-content" id='Bac-content'>
                                <h2>Bac Général Spé NSI & LLCER Anglais</h2>
                                <h3>LPO La Jetée</h3>
                                <h4>Sept 2019 - Juin 2022</h4>
                                <h4>Le François - Martinique</h4>
                                <p>Baccalauréat Général spécialités Numérique et sciences informatiques, et Langues, littératures, civilisations étrangères et régionales Anglais</p>
                                <div className="box-content-row" id="skills-list">
                                    <li>Python</li>
                                    <li>HTML</li>
                                    <li>CSS</li>
                                    <li>JavaScript</li>
                                    <li>Anglais</li>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

            </div>
        </section>
    )
}

export default Cursus;