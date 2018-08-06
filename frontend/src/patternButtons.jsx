import React from 'react';
import { Button, Container } from 'semantic-ui-react';
// Pretty sure I'm not following proper react style at all here, but we'll fix that later


export default class PatternButtonContainer extends React.Component {
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
                <Container textAlign='center'>
                    <Button.Group vertical>
                        {patterns.map(pattern => (
                            <PatternButton 
                                    key={pattern.display_name}
                                    info={pattern}
                            />
                        ))}
                    </Button.Group>
                </Container>
            );
        }    
    }
}



function PatternButton(props) {
    const info = props.info
    const url = "/api/v1/lights/set_pattern/" + info.id_name;
    return ( 
            <Button onClick={() => {fetch(url)} }
                    content={info.display_name}
                    color="Purple"
            />
    );
}




