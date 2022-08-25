import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Md5} from 'ts-md5'

@Injectable({
  providedIn: 'root'
})
export class OriginAPIService {
  

  constructor(private httpClient: HttpClient) { }

  register(username: string, email: string, password: string){
    const url =  'http://127.0.0.1:5000/register'
    password = Md5.hashStr(password)
    return this.httpClient.post(url, {"username": username, "email": email, "password": password}, {observe: "response"})
  }

  login(username: string, password: string){
    const url =  'http://127.0.0.1:5000/login'
    password = Md5.hashStr(password)
    return this.httpClient.post(url, {"username": username, "password": password}, {observe: "response", responseType: "json"})
  }
}
