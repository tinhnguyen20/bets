import { StyleSheet } from 'react-native';

import EditScreenInfo from '@/components/EditScreenInfo';
import Publicbets from '@/components/PublicBets';
import UserBetsPage from '@/components/UserBets';

import { Text, View } from '@/components/Themed';

export default function TabTwoScreen() {
  return (
    <View style={styles.container}>
      <Publicbets/>
      <Text style={styles.title}>User Bets</Text>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <UserBetsPage/>
      <UserBetsPage/>
      <UserBetsPage/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 30,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
