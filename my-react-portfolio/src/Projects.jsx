import './Projects.css'; 
import React, { useState, useEffect } from 'react';
import screengame2 from './assets/img/Screengame(2).png';
import screengame3 from './assets/img/Screengame(3).png';
import siteweb1 from './assets/img/siteweb1.png';
import siteweb2 from './assets/img/siteweb2.png';
import siteweb3 from './assets/img/siteweb3.png';
import lien from './assets/img/lien-externe.png';


function Accordion({ title, children }) {
  const [open, setOpen] = useState(false);
  return (
    <div className="accordion">
      <button
        className="accordion-title"
        onClick={() => setOpen((o) => !o)}
      >
        {title} {open ? "▲" : "▼"}
      </button>
        <div className={`accordion-content${open ? "" : " closed"}`}>
          {children}
        </div>
    </div>
  );
}

function MPMtest() {
  const testText = "Le chat bondit agilement sur la rambarde, défiant la gravité comme si le vide n'existait pas. Le vent du soir caressait les toits pendant que la lune, silencieuse, éclairait la scène d'un halo argenté. A quelques mètres, un chien le regardait fixement, prêt à défendre ses précieuses croquettes. Le duel était inévitable.";
  const [input, setInput] = useState('');
  const [startTime, setStartTime] = useState(null);
  const [endTime, setEndTime] = useState(null);
  const [isRunning, setIsRunning] = useState(false);
  const [errors, setErrors] = useState(0);
  const [finished, setFinished] = useState(false);

  // Calcul du temps réel
  useEffect(() => {
    if (isRunning && !finished && input.length > 0 && input.length <= testText.length) {
      if (input === testText) {
        setEndTime(Date.now());
        setIsRunning(false);
        setFinished(true);
      }
    }
  }, [input, isRunning, finished, testText]);

  // Calcul des erreurs à chaque frappe
  useEffect(() => {
    let err = 0;
    for (let i = 0; i < input.length; i++) {
      if (input[i] !== testText[i]) err++;
    }
    setErrors(err);
  }, [input, testText]);

  // Démarrage du test au premier caractère
  const handleChange = (e) => {
    if (!isRunning && e.target.value.length === 1) {
      setStartTime(Date.now());
      setIsRunning(true);
      setFinished(false);
      setEndTime(null);
      setErrors(0);
    }
    setInput(e.target.value);
  };

  // Calcul du temps écoulé
  const elapsed = isRunning
    ? ((Date.now() - startTime) / 1000).toFixed(2)
    : finished && endTime && startTime
    ? ((endTime - startTime) / 1000).toFixed(2)
    : 0;

  // Calcul du MPM (mots par minute)
  const wordsTyped = input.trim().split(/\s+/).length;
  const mpm = finished && startTime && endTime
    ? Math.round(wordsTyped / (((endTime - startTime) / 1000) / 60))
    : isRunning && startTime
    ? Math.round(wordsTyped / (((Date.now() - startTime) / 1000) / 60))
    : 0;

  // Affichage du texte avec indication des fautes
  function renderTestText() {
    return (
      <div className="mpm-text">
        {testText.split('').map((char, idx) => {
          let className = '';
          if (input[idx] === undefined) className = '';
          else if (input[idx] === char) className = 'correct';
          else{
            className = 'incorrect';
          }
          return (
            <span key={idx} className={className}>{char}</span>
          );
        })}
      </div>
    );
  }

  const handleReset = () => {
    setInput('');
    setStartTime(null);
    setEndTime(null);
    setIsRunning(false);
    setFinished(false);
    setErrors(0);
  };

  return (
    <div className="mpm-test">
      <h3>Recopier le texte ci-dessous le plus vite possible :</h3>
      {renderTestText()}
      <textarea
        value={input}
        onChange={handleChange}
        disabled={finished}
        placeholder="Tapez ici..."
        rows="5"
        cols="50"
        style={{ marginTop: "1em", fontSize: "1.1em", width: "100%" }}
      />
      <div className="mpm-controls">
        <button onClick={handleReset}>Réinitialiser</button>
        <p>MPM : {mpm}</p>
        <div className="mpm-info">
          <p>Temps écoulé : {elapsed} secondes</p>
          <p>Erreurs : {errors}</p>
          <p>{finished ? "Test terminé !" : "Test en cours..."}</p>
        </div>
      </div>
    </div>
  );
}

function ColorPicker(){
  const [color, setColor] = useState('#000000');

  function getTextColor(bgColor) {
    const hex = bgColor.replace('#', '');
    const r = parseInt(hex.substring(0,2), 16);
    const g = parseInt(hex.substring(2,4), 16);
    const b = parseInt(hex.substring(4,6), 16);
    const luminance = (0.299*r + 0.587*g + 0.114*b);
    return luminance > 150 ? '#222' : '#fff';
  }

  const handleColorChange = (event) => {
    setColor(event.target.value);
  };

  return (
    <div className="color-picker-container">
      <div
        className="color-display"
        onClick={() => navigator.clipboard.writeText(color)}
        style={{
          backgroundColor: color,
          color: getTextColor(color)
        }}
      >
        {color}
      </div>
      <label>Choisissez une couleur :</label>
      <input type='color' value={color} onChange={handleColorChange} />
    </div>
  );
}

function Placeholder() {
  return (
    <>
      <div className="defilement-lisse">
        <div className="contenu">
          En cours...
        </div>
      </div>
    </>
  );
}

const FigmaPrototype = () => {
  const [loaded, setLoaded] = useState(false);

  return (
    <div className="figma-container">
      {!loaded && <div className="placeholder">Chargement du prototype...</div>}
      <iframe
        title="Prototype Figma"
        onLoad={() => setLoaded(true)}
        className='figma-embed'
        style={{
          display: loaded ? 'block' : 'none',
        }}
        src="https://embed.figma.com/proto/LoHy5usBRI598X3Cg9i2JE/UI-UX-Gaspiypa?node-id=2-89&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=2%3A89&embed-host=share"
        allowFullScreen
      ></iframe>
    </div>
  );
};


function Projets() {
  return (
    <section id="projets">
      <div className="Bloc-content">
        <h1>Mes <span id='Colored'>Projets</span></h1>
        {/* <div className="image-wrapper">
        <img src="https://www.univ-smb.fr/espace-etudiant/wp-content/uploads/sites/81/2022/09/projet-etudiant.jpg" alt="" className='mainimg'/>
        </div> */}
        <p>Quelques mini-projets que j'ai pu réaliser :</p>
        <ul>
          <Accordion title="Projet React 1">
            <h2>Test de Mots par Minute (MPM)</h2>
            <MPMtest />
            <p>Un projet de test de mot par minute, il permet de tester la vitesse de frappe d'un utilisateur en lui demandant de taper un texte prédéfini.</p>
          </Accordion>
          <Accordion title="Projet React 2">
            <h2>Color Picker</h2>
            <ColorPicker />
            <p>Un sélecteur de couleur simple qui permet à l'utilisateur de choisir une couleur, l'afficher puis la copier dans son presse-papier.</p>
          </Accordion>
          
          {/* <Accordion title="Projet Angular">
            <Placeholder />
          </Accordion> */}

          <Accordion title="Projet UI/UX">
            <h2>Gaspiypa</h2>
            <FigmaPrototype />
            <br />
            <p>Gaspiypa est une application de gestion alimentaires. Elle permet aux utilisateurs de suivre et de réduire leur gaspillage alimentaire en fournissant des conseils personnalisés, des recettes et des statistiques sur leurs habitudes de consommation.</p>
            <p>Le prototype interactif complet est disponible sur Figma. Vous pouvez l'explorer en cliquant sur le lien ci-dessous :</p>
            <a href="https://www.figma.com/design/LoHy5usBRI598X3Cg9i2JE/UI-UX-Gaspiypa?node-id=2-89&t=Zu0LTVRSElo3BKhA-1" target="_blank" rel="noopener noreferrer">UI/UX Gaspiypa</a>
          </Accordion>

          <Accordion title="Projet Gaming">
            <h2>Cat'N Dog</h2>
            <div className="boximg">
              <img src= {screengame2} alt="Cat'N Dog screen1" className='screengame'/>
              <img src={screengame3} alt="Cat'N Dog screen2" className='screengame'/>
            </div>
            <p>Cat'N Dog est un jeu de fight-platformer où les joueurs incarnent un chat et un chien dans un univers coloré et dynamique.
              Le but du jeu est de voler la croquette adverse, pour cela vous devez éliminer votre adversaire pour débloquer l'accès au différente zone donnant accès à la croquette.
              Le jeu propose des combats en arène avec des mécaniques de plateforme, permettant aux joueurs de sauter, courir et combattre dans des environnements variés.</p>
            <br />
            <p>Télécharger la démo : (Pas encore disponible)</p>
          </Accordion>

          <p>Voici également quelques sites web sur lesquel j'ai pu travaillé :</p>

          <div className='grid-container' id='website'>
            <div className="website-box">
              <img src={siteweb1} alt="" />
              <div className="website-content">
                <h3>ICEA - Institut Catholique Européennes des Amériques</h3>
                <p>Site web institutionnel pour une école supérieure, présentant les programmes, les admissions et les actualités de l'institut.</p>
              </div>
              <a href="http://icea-edu.fr" target='_blank'><img src={lien} alt="" id='weblink' /></a>
            </div>

            <div className="website-box">
              <img src={siteweb2} alt="" />
              <div className="website-content">
                <h3>Nasdy - Agence de communication digitale</h3>
                <p>Site vitrine pour une agence de communication digitale, mettant en avant leurs services, leur portfolio et les témoignages clients.</p>
              </div>
                <a href="https://www.nasdy.fr/" target='_blank'><img src={lien} alt="" id='weblink' /></a>
            </div>

            <div className="website-box">
              <img src={siteweb3} alt="" />
              <div className="website-content">
                <h3>Akaya - Boutique en ligne de produits écoresponsables</h3>
                <p>Site e-commerce pour une boutique spécialisée dans les produits écoresponsables, avec un catalogue de produits, un système de paiement sécurisé et une interface utilisateur conviviale.</p>
              </div>
                <a href="https://akaya.odoo.com/" target='_blank'><img src={lien} alt="" id='weblink' /></a>
            </div>

          </div>
        </ul>
      </div>
    </section>
  );
}

export default Projets;