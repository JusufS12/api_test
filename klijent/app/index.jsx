import { Text, View, StyleSheet } from "react-native";
import { useEffect, useState } from "react";


export default function Index() {

  const [data, setData] = useState('');
  const [error, setError] = useState('');

  useEffect(async () => {
    try {
      const response = await fetch(
        'http://localhost:5000/api/data',
      );
      const json = await response.json();
      setData(json['message']);
    } catch (e) {
      setError(e);
    }
  }, [])


  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >

      <Text>{data ? data : error.toString()}</Text>
    </View>
  );
}
