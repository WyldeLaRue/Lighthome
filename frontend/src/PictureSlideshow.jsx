import React, { Component } from 'react'
import { Button, Divider, Image, Transition } from 'semantic-ui-react'

export default class PictureSlidshow extends Component {
    constructor(props) {
        super(props);
        this.state = {
            visible: true,
            active: 0,
            upNext: 1,
            loading: 2
        };
        this.pictureList = [
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
    }
  
    toggleVisibility() {
        this.setState({ visible: !this.state.visible })
    }

    
  render() {
    const { visible } = this.state

    return (
      <div>
        <Button content={visible ? 'Hide' : 'Show'} onClick={this.toggleVisibility} />
        <Divider hidden />
        <div style={{ position:'absolute' }}>
            <Transition visible={visible} animation='fade' duration={1500}>
              <Image centered size='small' src='/static/images/nature/1.jpeg' />
            </Transition>
        </div>
        <div style={{ position:'absolute' }}>
            <Transition visible={!visible} animation='fade' duration={1500}>
              <Image centered size='small' src='/static/images/nature/16.jpeg' />
            </Transition>
        </div>
        <div style={{ position:'absolute' }}>
            <Transition visible={!visible} animation='fade' duration={1500}>
              <Image centered size='small' src='/static/images/nature/16.jpeg' />
            </Transition>
        </div>
      </div>
    )
  }
}

