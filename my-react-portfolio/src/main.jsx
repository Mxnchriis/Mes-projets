import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ReactDOM from 'react-dom/client';
import './index.css'
import Header from './Header.jsx'
import Accueil from './Accueil.jsx'
import Apropos from './Apropos.jsx'
import Skills from './Skills.jsx'
import Cursus from './Cursus.jsx'
import Projets from './Projects.jsx'
import Contact from './Contact.jsx'
import Footer from './Footer.jsx'

if (sessionStorage.redirect) {
  const redirect = sessionStorage.redirect;
  delete sessionStorage.redirect;
  window.history.replaceState(null, '', redirect);
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter basename='/'>
      <Header />
      <Accueil />
      <Apropos/>
      <Cursus/>
      <Skills/>
      <Projets />
      {/* <Contact /> */}
      <Footer/>
    </BrowserRouter>
  </StrictMode>,
)
