import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class APIService {
  ENDPOINT = 'https://j9uq9rqpz9.execute-api.us-east-1.amazonaws.com/test/to-voice';
  constructor(private http:HttpClient) {}
  speak(data) {
    return this.http.post(this.ENDPOINT, data);
  }
}