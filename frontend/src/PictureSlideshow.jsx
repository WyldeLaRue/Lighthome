import React, { Component } from 'react'
import { Button, Divider, Image, Transition } from 'semantic-ui-react'

export default class PictureSlidshow extends Component {
  state = { visible: true }
  
  toggleVisibility = () => this.setState({ visible: !this.state.visible })

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
      </div>
    )
  }
}

// import React, { Component } from 'react'
// import { Form, Grid, Image, Transition } from 'semantic-ui-react'

// export default class TransitionExampleDuration extends Component {
//   state = { hide: 500, show: 500, visible: true }

//   handleChange = (e, { name, value }) => this.setState({ [name]: value })

//   toggleVisibility = () => this.setState({ visible: !this.state.visible })

//   render() {
//     const { hide, show, visible } = this.state

//     return (
//     <div>
//       <Grid columns={2}>
//         <Grid.Column as={Form}>
//           <Form.Input
//             label={`Hide duration: ${hide}ms `}
//             min={100}
//             max={5000}
//             name='hide'
//             onChange={this.handleChange}
//             step={100}
//             type='range'
//             value={hide}
//           />
//           <Form.Input
//             label={`Show duration: ${show}ms `}
//             min={100}
//             max={5000}
//             name='show'
//             onChange={this.handleChange}
//             step={100}
//             type='range'
//             value={show}
//           />
//           <Form.Button content='Run' onClick={this.toggleVisibility} />
//         </Grid.Column>
//             <p> Test </p>
//         <Grid.Column>

//         </Grid.Column>
//       </Grid>

//         <Transition duration={{ hide, show }} visible={visible}>
//           <Image src='https://react.semantic-ui.com/images/leaves/3.png' />
          
//         </Transition>
//     </div>

//     )
//   }
// }
// <Image src='/static/images/nature/1.jpeg' />