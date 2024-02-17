import React from 'react';
import { View, StyleSheet, Text } from 'react-native';

const HalfScreenComponent = () => {
  return (
    <View style={styles.container}>
      {/* Left Card */}
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Create a Bet</Text>
        {/* Content for left card */}
      </View>
      
      {/* Right Card */}
      <View style={styles.card}>
        <Text style={styles.cardTitle}>My Wallet</Text>
        <Text style={styles.cardTitle}>0 Bucks</Text>
        {/* Content for right card */}
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    display: 'flex', 
    flex: 1,
    flexGrow: 1,
    flexDirection: 'row',
  },
  card: {
    flex: 1,
    backgroundColor: 'lightblue',
    margin: 10,
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center',
  },
  cardTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 10,
    flexWrap: 'wrap',
    textAlign: 'center',
    alignItems: 'center',
  },
});

export default HalfScreenComponent;
