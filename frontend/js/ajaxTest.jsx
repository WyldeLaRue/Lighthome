import React from 'react';

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
                <button onClick={ () =>  {alert("hey")} }>
                    Push me for hey
                </button> 
                <button onClick={ () => {this.ajaxTest()} }>
                    Push me for ajax call
                </button> 
            </div>
        )
    }


    ajaxTest() {
        var testState = {test: 2};
        fetch("api/v1/lights/getPatternInfo")
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