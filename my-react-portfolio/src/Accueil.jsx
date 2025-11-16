import React, { useState, useEffect } from 'react';
// import './Body.css'; 
import './Accueil.css';
import selfie from './assets/img/selfie.jpg';
import { useNavigate } from 'react-router-dom';

function Accueil() {
  const [modalOpen, setModalOpen] = useState(false);
  const navigate = useNavigate();
  const [animate, setAnimate] = useState(false);

  function scrollToSection(id) {
    const section = document.getElementById(id);
    if (section) {
      section.scrollIntoView({ behavior: "smooth" });
    }
  }

  return (
    <section id="accueil">
      <div className="accueil-container">
        <div className="accueil-content">
          <img src={selfie} alt="" />
          <h1>
            Bienvenue sur mon <span id='Colored'>portfolio</span>
          </h1>
          <p>Découvrer mes projets et compétences en développement web.</p>
          <button
            className={animate ? "discover-btn animate" : "discover-btn"}
            onClick={() => {
              setAnimate(true);
              setTimeout(() => {
                scrollToSection("apropos");
              }, 600); // durée de l'animation en ms
            }}
          >
            Découvrir
          </button>
        </div>
        {modalOpen && <Modal onClose={() => setModalOpen(false)} />}
      </div>
    </section>
  );
}

export default Accueil;