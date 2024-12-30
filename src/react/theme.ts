import { createTheme} from "@mui/material";
import { green, blue } from "@mui/material/colors";

const theme = createTheme({
  palette: {
    mode: "dark",
    primary: green,
    secondary: blue,
    background: {
      default: "#303030",
    },
  },
  typography: {
    h1: {
      fontSize: "2.25rem",
      justifyContent: "Center"
    },
    h2: {
      fontSize: "1.75rem",
      justifyContent: "Center"
    }
  }
});


export default theme;
