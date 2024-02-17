import { StyleSheet } from 'react-native';
import HalfScreenComponent from '@/components/Bet/CreateBet';
import EditScreenInfo from '@/components/EditScreenInfo';
import UserBetsPage from '@/components/UserBets';
import { Text, View } from '@/components/Themed';

export default function TabOneScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Your Bets</Text>
      <HalfScreenComponent/>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <UserBetsPage/>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    paddingHorizontal: 30,
    flex: 1,
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
