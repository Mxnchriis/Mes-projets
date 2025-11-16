import linkedinLogo from './assets/contact/linkedin.png'
import githubLogo from './assets/contact/github.png'
import adresseLogo from './assets/contact/adresse.png'
import mobileLogo from './assets/contact/mobile.png'
import emailLogo from './assets/contact/email.png'
import MadaLogo from './assets/img/Mq.svg'
import './Footer.css'

function Footer() {

  function scrollToSection(id) {
    const section = document.getElementById(id);
    if (section) {
      section.scrollIntoView({ behavior: "smooth" });
    }
  }

  return (
    <>
      <div className="footer">
        <div className="footer-content">
          <div className="footer-title">
            <img src={MadaLogo} alt="GitHub Logo" className="github-logo" />
            <h1>AGOT Manchris</h1>
            <h2>Développeur Full-Stack en recherche d'alternance</h2>
          </div>

          <nav>
              <button onClick={() => scrollToSection("accueil") } id='btn-footer'>Accueil</button>
              <button onClick={() => scrollToSection("apropos")} id='btn-footer' >À propos</button>
              <button onClick={() => scrollToSection("parcours")} id='btn-footer' >Parcours</button>
              <button onClick={() => scrollToSection("skills")} id='btn-footer' >Skills</button>
              <button onClick={() => scrollToSection("projets")} id='btn-footer' >Projets</button>
              {/* <button onClick={() => scrollToSection("contact")} id='btn-footer' >Contact</button> */}
          </nav>

          <div className="adresse">
            <img src= {adresseLogo} alt="localisationLogo" />
            <h3>Le Crès 34920, France</h3>
          </div>

          <div className="footer-links">
          <a href="https://www.linkedin.com/in/manchris-a-144b79272/"><img src= {linkedinLogo} alt="LinkedIn Logo" className="linkedin-logo" /></a>
          <a href="https://github.com/Mxnchriis"><img src= {githubLogo} alt="" /></a>
          <a href="mailto:manchrisagot@gmail.com"><img src={emailLogo} alt="" /></a>
          <a href="tel:+33743607709"><img src={mobileLogo} alt="" /></a>
          </div>

          <h4>© 2025 AGOT Manchris. Tous droits réservés.</h4>
        </div>
      </div>
    </>
  )
}

export default Footer
