import React from 'react';

// Pretty sure I'm not following proper react style at all here, but we'll fix that later


export default class Pattern extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false, 
            patterns: []
        };
    }

    componentDidMount() {
        fetch("/api/v1/lights/get_pattern_library")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        patterns: Object.values(result)
                    });
                },
            )
    }   

    render() {
        const {error, isLoaded, patterns} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading......</div>;
        } else {
            return(
                <div>
                    {patterns.map(pattern => (
                        <PatternButton 
                                key={pattern.display_name}
                                info={pattern}
                        />
                    ))}
                </div>
            );
        }    
    }
}

function PatternButton(props) {
    const info = props.info
    const url = "/api/v1/lights/set_pattern/" + info.id_name;
    return ( 
            <button onClick={() => {fetch(url)} }>
                {info.display_name}
            </button>
    );
}