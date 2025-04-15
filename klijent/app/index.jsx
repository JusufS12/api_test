import { Text, View, ActivityIndicator } from "react-native";
import { useEffect, useState } from "react";


export default function Index() {

  const [data, setData] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/speedtest');
        const json = await response.json();
        setData(json);
      } catch (e) {
        setError(e.message || 'Unknown error');
      }
    };
  
    fetchData();
  }, []);
  

  return (
    <View
      style={{
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <View>
        {error ? error.toString() : (data ? 
        <>
          <Text>Download speed: {data['download']}</Text>
          <Text>Upload speed: {data['upload']}</Text>
        </>
         : <ActivityIndicator size="large" />)}
      </View>
    </View>
  );
}
