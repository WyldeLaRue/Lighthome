import React from 'react';
import Pattern from './patterns';
import AjaxTest from './ajaxTest';



export default class Page extends React.Component {
    render() {
        return (
            <div>
                <Navbar />
                <Body />
                <AjaxTest />
                <Pattern />
            </div> 
       )    

    }
}   


// function Navbar(props) {
//     return (
//         <p>
//             You made it
//         </p>
//     );
// }


function Navbar(props) {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
          <a className="navbar-brand" href="#">Navbar</a>
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>

          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav mr-auto">
              <li className="nav-item active">
                <a className="nav-link" href="#">Home <span className="sr-only">(current)</span></a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="#">Link</a>
              </li>
              <li className="nav-item dropdown">
                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  Dropdown
                </a>
                <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                  <a className="dropdown-item" href="#">Action</a>
                  <a className="dropdown-item" href="#">Another action</a>
                  <div className="dropdown-divider"></div>
                  <a className="dropdown-item" href="#">Something else here</a>
                </div>
              </li>
              <li className="nav-item">
                <a className="nav-link disabled" href="#">Disabled</a>
              </li>
            </ul>
          </div>
        </nav>
    );
}


function Body(props) {
    return (
        <div className="jumbotron">
            <div className="container">
                <h1>Very. Large. Title.</h1>
                <p>Are you ready to jump off a cliff? I probably should have a few paragraphs of placeholder text here.</p>
            </div>
        </div>
    )
}




