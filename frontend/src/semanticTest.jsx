import _ from 'lodash'
import React, { Component } from 'react'
import { Button, Image, List, Transition } from 'semantic-ui-react'

const users = ['ade', 'chris', 'christian', 'daniel', 'elliot', 'helen']
const images = [
            '/static/images/nature/1.jpeg',
            '/static/images/nature/1019.jpeg',
            '/static/images/nature/128.jpeg',
            '/static/images/nature/16.jpeg',
            '/static/images/nature/235.jpeg',
            '/static/images/nature/287.jpeg',
            '/static/images/nature/511.jpeg',
            '/static/images/nature/569.jpeg',
            '/static/images/nature/813.jpeg',
            '/static/images/nature/984.jpeg'
        ]

export default class Test extends Component {
    constructor(props) {
        super(props);
        this.state = { 
            items: [images[0]],
            current: 0,
            paused: false
        }
    }

    nextImage() {
        const current = (this.state.current + 1) % images.length
        this.setState({
            current: current,
            items: [images[current]]
        })
    }

    prevImage() {
        const current = (this.state.current + - 1 + images.length) % images.length
        this.setState({
            current: current,
            items: [images[current]]
        })
    }


    componentDidMount() {
        this.setState({paused: false});
        this.timer = setInterval(
            () => this.nextImage(),
            7000
        );
    }

    componentWillUnmount() {
       clearInterval(this.timer);
    }

  render() {
    const items = this.state.items
    const current = this.state.current
    const paused = this.state.paused

    // I really don't know why we need the => in the bottom
    return (
      <div>
        <Button.Group>
          <Button icon='minus' onClick={() => this.prevImage()} />
          <Button icon='plus' onClick={() => this.nextImage()} />
          <Button content={this.state.current} />
          <Button content={paused ? "Unpause" : "Pause"}  onClick={ () => this.setState({paused: !paused}) }/>
        </Button.Group>

        <Transition.Group as={List} duration={2000} divided size='huge' verticalAlign='middle'>
          {items.map(item => (
            <div style={{ position:'absolute' }} key={item}>
                <Image src={item} />
            </div>    
          ))}
        </Transition.Group>
      </div>
    )
  }
}