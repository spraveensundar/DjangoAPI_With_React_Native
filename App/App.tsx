import React, { useEffect } from "react";
import { View, Text, StyleSheet } from "react-native";

const App = () => {

    function initAppSettings() {
        console.log("Fetching Data")
        fetch("http://10.0.2.2:8000/api/v1.0/app/settings", { method: 'GET' })
            .then(res => {
                if (res.ok) {
                    return res.json()
                } else {
                    throw res.json()
                }
            })
            .then(json => {
                console.log("Good JSON")
                console.log(json)
            })
            .catch(error => {
                console.log("Bad JSON")
                console.log(error)
            })
    }

    useEffect(() => {
        initAppSettings()
    }, [])

    // OutPut 
    // backgroundColor: "#111111"
    // language: "English"
    // theme: "dark"

    return (
        <View style={styles.container}>
            <Text style={styles.text}>FIRST DJANGO APP</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#fff"
    },
    text: {
        fontSize: 18
    },
});

export default App;