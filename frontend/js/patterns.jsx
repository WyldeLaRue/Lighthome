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

    componentDidMount() {
        fetch("/api/v1/lights/getPatternInfo")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: Object.values(result)
                    });
                },
            )
    }   

    render() {
        const {error, isLoaded, items} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading......</div>;
        } else {
            return(
                <ul>
                    {items.map(item => (
                        <li key={item.key}>
                            {item.display_name}
                        </li>
                    ))}
                 </ul>
            );
        }    
    }
}