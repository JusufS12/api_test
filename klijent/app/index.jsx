import { View, ActivityIndicator } from "react-native";
import { useEffect, useState } from "react";


export default function Index() {

  const [data, setData] = useState('');
  const [error, setError] = useState('');

  useEffect(async () => {
    try {
      const response = await fetch('http://localhost:5000/api/speedtest');
      const json = await response.json();
      setData(json['download']);
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
      <View>
        {error ? error.toString() : (data ? data : <ActivityIndicator size="large" />)}
      </View>
    </View>
  );
}
