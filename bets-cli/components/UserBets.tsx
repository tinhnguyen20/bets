import React from 'react';
import { View, FlatList, StyleSheet, Text, SafeAreaView } from 'react-native';

// Sample data for the cards

interface Bet {
  id: string;
  title: string;
  description: string;
}

const data = [
  { id: '1', title: 'Who will win the next soccer match?', description: 'Predict the winning team of the upcoming soccer match.' },
  { id: '2', title: 'Will it rain tomorrow?', description: 'Bet on whether there will be rain tomorrow in your city.' },
  { id: '3', title: 'Is the stock market going to rise next week?', description: 'Make a prediction on the direction of the stock market for the upcoming week.' },
  { id: '4', title: 'Will the new movie be a box office hit?', description: 'Predict whether the latest movie release will be a box office success.' },
  { id: '5', title: 'Who will be the next president?', description: 'Bet on the next president in the upcoming election.' },
  { id: '6', title: 'Will it snow on Christmas Day?', description: 'Bet on whether there will be snowfall on Christmas Day.' },
  { id: '7', title: 'Which team will win the championship?', description: 'Predict the winning team of the upcoming championship.' },
  { id: '8', title: 'Will the new product be popular?', description: 'Make a prediction on the popularity of the new product.' },
  { id: '9', title: 'Who will score the first goal?', description: 'Bet on which player will score the first goal in the match.' },
  { id: '10', title: 'Will the price of oil increase?', description: 'Predict whether the price of oil will increase in the next month.' },
  { id: '11', title: 'Who will win the Oscar for Best Actor?', description: 'Bet on the actor who will win the Oscar for Best Actor.' },
  { id: '12', title: 'Will the company announce dividends?', description: 'Predict whether the company will announce dividends this quarter.' },
  { id: '13', title: 'Will it be a white Christmas?', description: 'Bet on whether there will be snow on the ground on Christmas Day.' },
  { id: '14', title: 'Which team will score first?', description: 'Predict the team that will score the first point in the match.' },
  { id: '15', title: 'Will the interest rates go up?', description: 'Make a prediction on whether the interest rates will increase.' },
  { id: '16', title: 'Who will win the Nobel Prize in Literature?', description: 'Bet on the author who will win the Nobel Prize in Literature.' },
  { id: '17', title: 'Will the company release a new product?', description: 'Predict whether the company will release a new product next quarter.' },
  { id: '18', title: 'Who will win the next Formula 1 race?', description: 'Bet on the driver who will win the next Formula 1 race.' },
  { id: '19', title: 'Will the company meet its revenue target?', description: 'Make a prediction on whether the company will meet its revenue target this year.' },
  { id: '20', title: 'Will there be a major earthquake next month?', description: 'Bet on whether there will be a major earthquake next month.' },
];

const UserBetsPage = () => {
  // Render each card item
  const renderItem = ({ item }) => (
    <View style={styles.card}>
      {/* Render your card content here */}
      <Text style={styles.title}>{item.title}</Text>
      <Text style={styles.description}>{item.description}</Text>
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      {/* FlatList for the scrollable grid view */}
      <FlatList
        horizontal
        data={data}
        renderItem={renderItem}
        keyExtractor={item => item.id}
        contentContainerStyle={{ flexGrow: 1}}
        showsHorizontalScrollIndicator={false}
      />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingHorizontal: 30,
  },
  card: {
    flex: 1,
    maxWidth: 300,
    maxHeight: 200,
    marginHorizontal: 10,
    backgroundColor: 'lightblue',
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 10,
  },
  title: {
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 5,
    flexWrap: 'wrap',
    textAlign: 'center',
    alignItems: 'center',
  },
  description: {
    fontSize: 16,
    flexWrap: 'wrap',
    textAlign: 'center',
    alignItems: 'center',
  },
});

export default UserBetsPage;
