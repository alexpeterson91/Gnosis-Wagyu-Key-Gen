import { createTheme } from "@material-ui/core";
import { amber, blue } from "@material-ui/core/colors";



const theme = createTheme({
  palette: {
    type: "dark",
    primary: amber,
    secondary: blue,
  },
  typography: {
    h1: {
      fontSize: "36px"
    },
    h2: {
      fontSize: "20px"
    }
  }
});


export default theme;