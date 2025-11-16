import './Apropos.css'
import linkedinLogo from './assets/contact/linkedin.png'
import githubLogo from './assets/contact/github.png'
import emailLogo from './assets/contact/email.png'
import mobileLogo from './assets/contact/mobile.png'
import UKLogo from './assets/img/UK.png'
import SpainLogo from './assets/img/Spain.png'
import PermisBLogo from './assets/img/PermisB.jpg'

function ImageModal({ src, alt, open, onClose }) {
  if (!open) return null;
  return (
    <div
      className="modal-backdrop"
      onClick={onClose}
      style={{
        position: "fixed",
        top: 0, left: 0, right: 0, bottom: 0,
        background: "rgba(0,0,0,0.7)",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        zIndex: 1000
      }}
    >
      <img
        src={src}
        alt={alt}
        style={{
          maxWidth: "90vw",
          maxHeight: "90vh",
          borderRadius: "10px",
          boxShadow: "0 0 30px #000"
        }}
        onClick={e => e.stopPropagation()} // Pour ne pas fermer en cliquant sur la photo
      />
    </div>
  );
}

function ImageWrapper({ src, alt }) {
  const [modalOpen, setModalOpen] = useState(false);

  return (
    <>
      <div className="image-wrapper">
        <div className="blur-background"></div>
        <img
          src={src}
          alt={alt}
          id='mainimg'
          style={{ cursor: "pointer" }}
          onClick={() => setModalOpen(true)}
        />
      </div>
      <ImageModal src={src} alt={alt} open={modalOpen} onClose={() => setModalOpen(false)} />
    </>
  );
}

function Apropos() {
  return (
    <section id="apropos">
            <div className="Bloc-content">
            <h1>
                Qui <span id='Colored'>suis-je</span> ?
            </h1>
            <p>
                Je suis AGOT Manchris, un jeune développeur de 20ans passionné par la création d'applications web modernes et interactives sur Montpellier.
                Mon parcours m'a permis d'acquérir des compétences solides en développement front-end et back-end, 
                ainsi qu'une compréhension approfondie des technologies web.
            </p>

            <div className="grid-container">

                <div className="box-content-column" id='info-perso' >
                <h2><span id='Colored2'>AGOT</span> Manchris</h2>
                <h2>DÉVELOPPEUR <span className='fullstack' id='Colored2'>FULL-STACK</span></h2>
                <h2><span id='Colored2'>20</span> ans</h2>
                <h2>Le Crès 34920, <span id='Colored2'>France</span></h2>
                </div>

                <div className="box-content-column">
                {/* <ImageWrapper src={selfie} alt="" /> */}

                <div className="box-content-column" id='links-container'>
                    <a href="https://www.linkedin.com/in/manchris-a-144b79272/" style={{ textDecoration: 'none' }}>
                    <div className="box-content-row">
                        <img src={linkedinLogo} alt="LinkedIn Logo" className="linkedin-logo" /><h3>LinkedIn</h3>
                    </div>
                    </a>
                    <a href="https://github.com/Mxnchriis" style={{ textDecoration: 'none' }}>
                    <div className="box-content-row">
                        <img src={githubLogo} alt="" /><h3>GitHub</h3>
                    </div>
                    </a>
                    <a href="mailto:manchrisagot@gmail.com" style={{ textDecoration: 'none' }}>
                    <div className="box-content-row">
                        <img src={emailLogo} alt="" /><h3>E-mail</h3>
                    </div>
                    </a>
                    <a href="tel:+33743607709" style={{ textDecoration: 'none' }}>
                    <div className="box-content-row">
                        <img src={mobileLogo} alt="" /><h3>Téléphone</h3>
                    </div>
                    </a>
                </div>

                </div>

            </div>

            <h2 id='info-utile'>Infos utiles</h2>

            <div className="box-content-row" id='card-display'>
                <div className="card-product">
                <img src={UKLogo} alt="United Kingdom" />
                  <div className="card-product-infos">
                      <h3>Anglais</h3>
                      <p>Niveau B2</p>
                  </div>
                </div>

                <div className="card-product">
                <img src={SpainLogo} alt="Spain" />
                  <div className="card-product-infos">
                      <h3>Espagnol</h3>
                      <p>Niveau A2</p>
                  </div>
                </div>

                <div className="card-product">
                <img src={PermisBLogo} alt="Driver Licence" />
                  <div className="card-product-infos">
                      <h3>Permis B</h3>
                      <p>Non-Véhiculé</p>
                  </div>
                </div>
            </div>
            </div>
        </section>
  )
}

export default Apropos;