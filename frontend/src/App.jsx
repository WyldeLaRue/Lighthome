// App.jsx
import React from 'react';
import Page from './page';
// import Test from './semanticTest';
import PatternButtonContainer from './patterns';
import AjaxTest from './ajaxTest';
// import PictureSlidshow from './PictureSlideshow';
import { Container, Divider, Header } from 'semantic-ui-react';

export default class App extends React.Component {
    render () {
        return (
            <div>
                <Page />
                <AjaxTest />
                <PatternButtonContainer />
                <p> test????? </p>
            </div>
        );
    }
}

             //   <Container>
             //       <Test />
             //   </Container>

                // <Divider />
                //     <Header as='h1'>Debug</Header>
                // <Divider />