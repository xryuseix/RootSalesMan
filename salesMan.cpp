#include <iostream>
#include <bitset>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <climits>
using namespace std;

#define rep(i,n) for(int i = 0; i < (n); ++i)
const int INF = INT_MAX;

vector<int> intSplit(string& input, char delimiter) {
    istringstream stream(input);
    string field;
    vector<int> result;
    while (getline(stream, field, delimiter)) {
        result.push_back(stoi(field));
    }
    return result;
}

vector<string> charSplit(string& input, char delimiter) {
    istringstream stream(input);
    string field;
    vector<string> result;
    while (getline(stream, field, delimiter)) {
        result.push_back(field);
    }
    return result;
}
// https://www.google.com/maps/dir/?api=1&origin=横浜駅&destination=東京駅&waypoints=川崎駅|品川駅&travelmode=driving
void makeURL(vector<int> route) {
    ifstream ifs("destination.csv");
    string line;
    getline(ifs, line);
    vector<string> pos = charSplit(line, ',');
    string url = "https://www.google.com/maps/dir/?api=1&origin=" + pos[route[0]] + "&destination=" + pos[route[0]] + "&waypoints=";
    for(int i = 1; i < route.size() - 1; i++) {
        if(i == 1) url += pos[route[i]];
        else url += '|' + pos[route[i]];
    }
    url += "&travelmode=walking";
    cout << url << endl;
}

int main(void) {
    ifstream ifs("distance.csv");
    string line;

    vector<vector<int>> dist;

    while (getline(ifs, line)) {
        vector<int> tmp = intSplit(line, ',');
        dist.push_back(tmp);
    }

    int N = dist.size();
    vector<int> dp(1<<N, INF);
    vector<int> lastPos(1<<N,0);
    vector<int> route(1,0);
    dp[1]=0;
    for(int i = 1; i < (1<<N); i++){
        if(dp[i] == INF) continue;
        rep(j,N) {
            if(i&(1<<j)) continue;
            if(dp[i|1<<j] > dp[i] + dist[lastPos[i]][j]) {
                dp[i|1<<j] = dp[i] + dist[lastPos[i]][j];
                lastPos[i|1<<j] = j;
            }
            
        }
    }
    // ルートの総和
    cout << "総走行距離 : " << (dp[(1<<N) - 1] + dist[lastPos[(1<<N) - 1]][0])/1000.0 << "km" << endl;
    
    int lastV=(1<<N) - 1;
    while(lastV != 0) {
        route.push_back(lastPos[lastV]);
        lastV = lastV^(1<<lastPos[lastV]);
    }
    reverse(route.begin(), route.end());
    // 最短経路
    // rep(i,route.size()) {
    //     cout << route[i] << " ";
    // }
    // cout << endl;
    makeURL(route);
}