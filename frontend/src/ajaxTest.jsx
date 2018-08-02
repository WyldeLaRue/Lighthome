import React from 'react';
import { Button } from 'semantic-ui-react';


export default class AjaxTest extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false, 
            items: []
        };
    }

    simpleTest() {
        alert("yo");
    }

    render() {
        return(
            <div>
                <Button onClick={ () =>  {alert("hey")} }
                        content='click here for hey'
                 />
                <Button onClick={ () => {this.ajaxTest()} }
                        content='Push me for ajax call'
                />
            </div>
        );
    }


    ajaxTest() {
        var testState = {test: 2};
        fetch("api/v1/lights/get_pattern_library")
            .then(res => res.json())
            .then(
                (result) => {
                    console.log(result);
                    alert(result.keys);
                },
                (error) => {
                    alert("failed?")
                }
            )
    }


}