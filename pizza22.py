/**
 * @format
 */

import {AppRegistry} from 'react-native';
import App from './App';
import {name as appName} from './app.json';

//added 11/8 
import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';

AppRegistry.registerComponent(appName, () => App);
