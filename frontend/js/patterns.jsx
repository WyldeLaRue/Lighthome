import React from 'react';



export default class Pattern extends React.Component {
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

    // componentDidMount() {
    //     fetch("api/v1/lights/getPatternInfo")
    //         .then(res => res.json())
    //         .then(
    //             (result) => {
    //                 this.setState({
    //                     isLoaded: true,
    //                     items: result.items
    //                 });
    //             },
    //         )
    // }   

    // render() {
    //     const {error, isLoaded, items} = this.state;
    //     if (error) {
    //         return <div>Error: {error.message}</div>;
    //     } else if (!isLoaded) {
    //         return <div>Loading...</div>;
    //     } else {
    //         return(
    //             <div>
    //                 <p> test </p>
    //                 <ul>
    //                     {items.map(item => (
    //                         <li key={item.display_name}>
    //                             {item.display_name}
    //                         </li>
    //                     ))}
    //                  </ul>
    //             </div>  
    //         );
    //     }    
    // }
}