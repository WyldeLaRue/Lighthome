// App.jsx
import React from 'react';
import Page from './page';
// import Test from './semanticTest';
import PatternButtonContainer from './patternButtons';
import AjaxTest from './ajaxTest';
// import PictureSlidshow from './PictureSlideshow';
import { Container, Divider, Header } from 'semantic-ui-react';

// scp /Users/tristan/projects/homepage/frontend/static/dist/bundle.js pi@fishflag:~/projects/homepage/frontend/static/dist/bundle.js
export default class App extends React.Component {
    render () {
        return (
            <div>
                <Page />
                <AjaxTest />
                <Divider section />
                    <PatternButtonContainer />
                <Divider section />
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