import './Skills.css'
import React, { useState, useEffect } from 'react';
import pythonLogo from './assets/python.png';
import htmlLogo from './assets/html.png';
import cssLogo from './assets/css.png';
import jsLogo from './assets/js.png';
import javaLogo from './assets/java.svg';
import nodeLogo from './assets/node.png';
import angularLogo from './assets/angular.png';
import cLogo from './assets/c.png';
import cppLogo from './assets/cpp.png';
import csharpLogo from './assets/csharp.png';
import phpLogo from './assets/php.png';
import sqlLogo from './assets/sql.png';
import bashLogo from './assets/bash.png';
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import githubLogo from './assets/contact/github.png'
import wwwLogo from './assets/www.png'
import figmaLogo from './assets/figma.png'
import programpooLogo from './assets/programpoo.png'
import serveurLogo from './assets/img/serveur.png'
import office365Logo from './assets/img/office365.png'


const langImages = [
  { src: pythonLogo, alt: "Python" },
  { src: htmlLogo, alt: "HTML" },
  { src: cssLogo, alt: "CSS" },
  { src: jsLogo, alt: "JavaScript" },
  { src: javaLogo, alt: "Java" },
  { src: reactLogo, alt: "React" },
  { src: nodeLogo, alt: "Node.js" },
  { src: viteLogo, alt: "Vite" },
  { src: angularLogo, alt: "Angular" },
  { src: cLogo, alt: "C" },
  { src: cppLogo, alt: "C++" },
  { src: csharpLogo, alt: "C#" },
  { src: phpLogo, alt: "PHP" },
  { src: sqlLogo, alt: "SQL" },
  { src: bashLogo, alt: "Bash" },
];

function Carrousel() {
  const [index, setIndex] = useState(0);
  const [dragStartX, setDragStartX] = useState(null);

  // Défilement automatique
  useEffect(() => {
    const timer = setInterval(() => {
      setIndex((prevIndex) => (prevIndex + 1) % langImages.length);
    }, 5000);
    return () => clearInterval(timer);
  }, []);

  // Empêche le drag d'image natif
  const preventDragHandler = (e) => {
    e.preventDefault();
  };

  // Gestion du glissement (touch)
  const handleTouchStart = (e) => {
    setDragStartX(e.touches[0].clientX);
  };

  const handleTouchEnd = (e) => {
    if (dragStartX === null) return;
    const dragEndX = e.changedTouches[0].clientX;
    const diff = dragEndX - dragStartX;
    if (Math.abs(diff) > 40) {
      if (diff > 0) {
        setIndex((index - 1 + langImages.length) % langImages.length); // swipe droite
      } else {
        setIndex((index + 1) % langImages.length); // swipe gauche
      }
    }
    setDragStartX(null);
  };

  // Gestion du glissement (souris)
  const handleMouseDown = (e) => {
    setDragStartX(e.clientX);
  };
  const handleMouseUp = (e) => {
    if (dragStartX === null) return;
    const dragEndX = e.clientX;
    const diff = dragEndX - dragStartX;
    if (Math.abs(diff) > 40) {
      if (diff > 0) {
        setIndex((index - 1 + langImages.length) % langImages.length);
      } else {
        setIndex((index + 1) % langImages.length);
      }
    }
    setDragStartX(null);
  };

  return (
    <div
      className="carrousel"
      onTouchStart={handleTouchStart}
      onTouchEnd={handleTouchEnd}
      onMouseDown={handleMouseDown}
      onMouseUp={handleMouseUp}
      style={{ userSelect: "none", cursor: "grab" }}
    >
      <div className="carrousel-bloc">
        <img
          src={langImages[(index - 1 + langImages.length) % langImages.length].src}
          alt={langImages[(index - 1 + langImages.length) % langImages.length].alt}
          style={{ opacity: 0.5 }}
          draggable={false}
          onDragStart={preventDragHandler}
        />
        <img
          src={langImages[index].src}
          alt={langImages[index].alt}
          className='mainlogo'
          draggable={false}
          onDragStart={preventDragHandler}
        />
        <img
          src={langImages[(index + 1) % langImages.length].src}
          alt={langImages[(index + 1) % langImages.length].alt}
          style={{ opacity: 0.5 }}
          draggable={false}
          onDragStart={preventDragHandler}
        />
      </div>
      <div className='programName'>{langImages[index].alt}</div>
    </div>
  );
}

function Skills(){
    return (
        <section id="skills">
            <div className="Bloc-content">
                <h1>Mes</h1>
                <h1 id='Colored'>Compétences</h1>
                <p>Voici un aperçu des compétences techniques que j'ai développées au fil de mon parcours.</p>
                <div className="grid-container" id='skills-container'>
                    <div className="box-content-column" id='skill-box'>
                        <img src={wwwLogo} alt="Logo" />
                        <h2>Développement Web</h2>
                        <p>Création de sites web responsives et interactifs en utilisant HTML, CSS, JavaScript, des frameworks modernes comme React et Angular etc...</p>
                        <div className="box-content-row" id="skills-list">
                            <li>HTML</li>
                            <li>CSS</li>
                            <li>JavaScript</li>
                            <li>PHP</li>
                            <li>React</li>
                            <li>Angular</li>
                            <li>Vite</li>
                            <li>Node.js</li>
                            <li>Wordpress</li>
                            <li>Odoo</li>
                        </div>
                    </div>
                    <div className="box-content-column" id='skill-box'>
                        <img src={programpooLogo} alt="Logo" />
                        <h2>Progammation et POO</h2>
                        <p>Maîtrise des concepts de la programmation de base et de l'orientée objet (POO) pour structurer et organiser le code de manière efficace et réutilisable.</p>
                        <div className="box-content-row" id="skills-list">
                            <li>Python</li>
                            <li>Java</li>
                            <li>JavaScript</li>
                            <li>C</li>
                            <li>C++</li>
                            <li>C#</li>
                            <li>PHP</li>
                            <li>Bash</li>
                        </div>
                    </div>
                    {/* <div className="box-content-column" id='skill-box'>
                    <img src={jsLogo} alt="Logo" />
                    <h2>Intégration d'API et gestion des données</h2>
                    <p>Intégration d'API tierces et gestion des données en utilisant des outils comme Axios et Fetch pour assurer une communication fluide entre le front-end et le back-end.</p>
                    </div> */}
                    <div className="box-content-column" id='skill-box'>
                        <img src={sqlLogo} alt="Logo" />
                        <h2>Conception de bases de données</h2>
                        <p>Conception et gestion de bases de données relationnelles et non relationnelles, ainsi que le développement de serveurs back-end.</p>
                        <div className="box-content-row" id="skills-list">
                            <li>MySQL</li>
                            <li>SQLite</li>
                            <li>PHP</li>
                            <li>Python</li>
                            <li>Node.js</li>
                            <li>Symfony</li>
                            <li>Odoo.sh</li>
                        </div>
                    </div>
                    <div className="box-content-column" id="skill-box">
                        <img src={figmaLogo} alt="Logo" />
                        <h2>UI/UX Design</h2>
                        <p>Compétences en design d'interface utilisateur et en expérience utilisateur pour créer des designs attrayants et faciles à utiliser.</p>
                        <div className="box-content-row" id="skills-list">
                            <li>Figma</li>
                            <li>Canvas</li>
                            <li>Photoshop</li>
                            <li>Aseprite</li>
                        </div>
                    </div>
                    <div className="box-content-column" id='skill-box'>
                        <img src={githubLogo} alt="Logo" />
                        <h2>Contrôle de version</h2>
                        <p>Maîtrise de Git pour le contrôle de version, la collaboration en équipe et la gestion efficace des projets de développement.</p>
                        <div className="box-content-row" id="skills-list">
                            <li>Git</li>
                            <li>GitHub</li>
                            <li>GitLab</li>
                            <li>GitHub Desktop</li>
                        </div>
                    </div>
                    <div className="box-content-column" id="skill-box">
                        <img src={bashLogo} alt="Logo" />
                        <h2>Système d'exploitation</h2>
                        <p>Compétences en administration et utilisation des systèmes d'exploitation Linux et Windows, y compris la gestion des fichiers, des processus et des permissions.</p>
                        <div className="box-content-row" id="skills-list">
                            <li>VirtualBox</li>
                            <li>Linux (Ubuntu)</li>
                            <li>Windows</li>
                            <li>Cmd</li>
                            <li>PowerShell</li>
                            <li>SSH</li>
                            <li>PuTTY</li>
                        </div>
                    </div>
                    <div className="box-content-column" id='skill-box'>
                        <img src={serveurLogo} alt="Logo" />
                        <h2>Réseaux et Sécurité</h2>
                        <p>Connaissances de base en réseaux informatiques, y compris les protocoles, la configuration et la sécurité des réseaux.</p>
                        <div className="box-content-row" id="skills-list">
                            <li>Notions de base en réseaux</li>
                            <li>Notions de base en cybersécurité</li>
                            <li>Configuration de routeurs et switches</li>
                            <li>Firewall</li>
                            <li>VPN</li>
                        </div>
                    </div>
                    <div className="box-content-column" id='skill-box'>
                        <img src={office365Logo} alt="Logo" />
                        <h2>Office 365</h2>
                        <p>Maîtrise des outils de la suite Office 365, y compris Word, Excel, PowerPoint et Outlook pour la productivité et la collaboration.</p>
                        <div className="box-content-row" id="skills-list">
                            <li>Word</li>
                            <li>Excel</li>
                            <li>PowerPoint</li>
                            <li>Outlook</li>
                            <li>OneNote</li>
                            <li>Teams</li>
                        </div>
                    </div>
                </div>
            </div>

            <div className="Bloc-content">
              <h2>Mes langages de <span id='Colored2'>programmation</span></h2>
              <ul>
                  <li>Python, HTML, CSS, JavaScript, Java</li>
                  <li>Frameworks : React, Node.js, Angular</li>
                  <li>C, C++, C#</li>
                  <li>PHP, SQL, Bash</li>
              </ul>
              {/* <Carrousel /> */}

              <div className="defilement-lisse">
                <div className="group-card-language">
                  <div className="card-language">
                    <img src={pythonLogo} alt="Python" />
                    <h3>Python</h3>
                  </div>

                  <div className="card-language">
                    <img src={htmlLogo} alt="HTML" />
                    <h3>HTML</h3>
                  </div>

                  <div className="card-language">
                    <img src={cssLogo} alt="CSS" />
                    <h3>CSS</h3>
                  </div>

                  <div className="card-language">
                    <img src={jsLogo} alt="JavaScript" />
                    <h3>JavaScript</h3>
                  </div>

                  <div className="card-language">
                    <img src={javaLogo} alt="Java" />
                    <h3>Java</h3>
                  </div>

                  <div className="card-language">
                    <img src={phpLogo} alt="PHP" />
                    <h3>PHP</h3>
                  </div>

                  <div className="card-language">
                    <img src={sqlLogo} alt="SQL" />
                    <h3>SQL</h3>
                  </div>

                  <div className="card-language">
                    <img src={reactLogo} alt="React" />
                    <h3>React</h3>
                  </div>

                  <div className="card-language">
                    <img src={viteLogo} alt="Vite" />
                    <h3>Vite</h3>
                  </div>

                  <div className="card-language">
                    <img src={nodeLogo} alt="Node.js" />
                    <h3>Node.js</h3>
                  </div>

                  <div className="card-language">
                    <img src={angularLogo} alt="Angular" />
                    <h3>Angular</h3>
                  </div>

                  <div className="card-language">
                    <img src={cLogo} alt="C" />
                    <h3>C</h3>
                  </div>

                  <div className="card-language">
                    <img src={cppLogo} alt="C++" />
                    <h3>C++</h3>
                  </div>

                  <div className="card-language">
                    <img src={csharpLogo} alt="C#" />
                    <h3>C#</h3>
                  </div>

                  <div className="card-language">
                    <img src={bashLogo} alt="Bash" />
                    <h3>Bash</h3>
                  </div>

                </div>
              </div>
            </div>

            <div className="Bloc-content" id='outils'>
              <h2>Mes <span id='Colored2'>outils</span> de développement</h2>
              {/* <ul>
                  <li>Visual Studio Code</li>
                  <li>Git, GitHub</li>
                  <li>Figma, Canvas</li>
                  <li>VirtualBox, PuTTY </li>
                  <li>Wordpress, Odoo</li>
                  <li>Office 365 (Word, Excel, PowerPoint, ect...)</li>
                  <li>ChatGPT, Copilot</li>
                  <li>Unreal Engine 5, Unity</li>
              </ul> */}

              <div className="grid-app" id='gridapp1'>
                <div className="dev-app-box" id='vscode'>
                  <div className="dev-app-content">
                    <h3 id='h3dev'>Visual Studio Code</h3>
                    <p>Mon application principale de dev</p>
                  </div>
                </div>

                <div className="dev-app-box" id='git'>
                  <div className="dev-app-content">
                    <h3 id='h3dev'>Git/Github</h3>
                    <p>Mes outils de versionning</p>
                  </div>
                </div>
              </div>


              <div className="grid-app" id='gridapp2'> 
                <div className="dev-app-box" id='ia'>
                  <div className="dev-app-content">
                    <h3 id='h3dev'>ChatGPT, Copilot</h3>
                    <p>Intelligence Artificielle m'aidant au quotidient</p>
                  </div>
                </div>


                <div className="dev-app-box" id='vm'>
                  <div className="dev-app-content">
                    <h3 id='h3dev'>VirtualBox, PuTTY</h3>
                    <p>Système d'exploitation Linux et SSH</p>
                  </div>
                </div>

                <div className="dev-app-box" id='ue5'>
                  <div className="dev-app-content">
                    <h3 id='h3dev'>Unreal Engine 5, Unity</h3>
                    <p>Mes outils de création de jeux-vidéos</p>
                  </div>
                </div>
              </div>

              <div className="grid-app" id='gridapp3'>
                <div className="dev-app-box" id='nocode'>
                  <div className="dev-app-content">
                    <h3 id='h3dev'>Wordpress, Odoo</h3>
                    <p>Mes outils de No-code </p>
                  </div>
                </div>

                <div className="dev-app-box" id='figma'>
                  <div className="dev-app-content">
                    <h3 id='h3dev'>Figma, Canvas</h3>
                    <p>Mes applis de designs</p>
                  </div>
                </div>
                
                <div className="dev-app-box" id='office'>
                  <div className="dev-app-content">
                    <h3 id='h3dev'>Office 365 (Word, Excel, PowerPoint, ect...)</h3>
                    <p>Prise de Notes et Présentation</p>
                  </div>
                </div>


              </div>
            </div>
        </section>
    )
}

export default Skills;