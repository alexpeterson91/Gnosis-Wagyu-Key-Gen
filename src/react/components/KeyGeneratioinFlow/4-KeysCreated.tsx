import { Box, Grid, Typography } from '@material-ui/core';
import { shell } from 'electron';
import React, { FC, ReactElement } from 'react';
import styled from 'styled-components';
import { Network } from '../../types';
import VersionFooter from '../VersionFooter';

type KeysCreatedProps = {
  folderPath: string,
  network: Network
}

const LoudText = styled(Typography)`
  color: cyan;
  text-align: left;
`;

const KeysCreated: FC<KeysCreatedProps> = (props): ReactElement => {

  return (
    <Grid container>
      <Grid item xs={1} />
      <Grid item xs={10}>
          <Box sx={{ m: 2 }}>
            <Typography variant="body1" align="left">
              Your keys have been created here: '{props.folderPath}'
            </Typography>
          </Box>
          <Box sx={{ m: 2 }}>
            <Typography variant="body1" align="left">
              There are two different files, here is a description of each:
            </Typography>
            <LoudText>Keystore file(s) (ex. keystore-xxxxxxx.json)</LoudText>
            <Typography variant="body2" align="left">
              This file controls your ability to sign transactions.  It will be required to set up your validator.  Do not share with anyone.  It can be recreated from your secret recovery phrase if necessary.
            </Typography>
            <LoudText>Deposit data file(s) (ex. deposit_data-xxxxxx.json)</LoudText>
            <Typography variant="body2" align="left">
              This file represents public information about your validator.  It will be required to execute your deposit through the Ethereum Launchpad.  It can be recreated from your secret recovery phrase if necessary.
            </Typography>
          </Box>
          <Box sx={{ m: 2 }}>
            <LoudText>Secret Recovery Phrase (24 words)</LoudText>
            <Typography variant="body2" align="left">
              This was the first thing you created.  It is also known as a "mnemonic" or "seed phrase".  You'll need this to withdraw your funds.  Keep multiple copies in different physical locations safe from theft, fire, water and other hazards. Keep it private.  There is no way to recover this.
            </Typography>
          </Box>
      </Grid>
      <Grid item xs={1} />
      <VersionFooter />
    </Grid>
  );
}

export default KeysCreated;