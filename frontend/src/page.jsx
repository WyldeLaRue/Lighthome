import React, { Component } from 'react'
import { Menu, Segment, Header, Divider} from 'semantic-ui-react'



export default class Page extends React.Component {
    render() {
        return (
            <div>
                <DarkNavbar />
                <Body />
                <Divider hidden />
            </div> 
       )    

    }
}   



class DarkNavbar extends Component {
  state = { activeItem: 'home' }

  handleItemClick = (e, { name }) => this.setState({ activeItem: name })

  render() {
    const { activeItem } = this.state

    return (
      <Menu inverted>
        <Menu.Item name='home' active={activeItem === 'home'} onClick={this.handleItemClick} />
        <Menu.Item
          name='messages'
          active={activeItem === 'messages'}
          onClick={this.handleItemClick}
        />
        <Menu.Item
          name='friends'
          active={activeItem === 'friends'}
          onClick={this.handleItemClick}
        />
      </Menu>
    )
  }
}




const Body = () => (
  <Segment color='Orange' textAlign='center'>
    <Header as='h1'>Somewhat. Large. Title.</Header>
    <p> It's 96 degrees and I'm slowly dying. Here is some placeholder text.</p>
</Segment>
)





