//
//  RecipeAPI.swift
//  JGMTDR
//
//  Created by Payton Pehrson on 11/9/20.
//  Copyright © 2020 Payton Pehrson. All rights reserved.
//

import Foundation

struct RecipeAPI {
    //Here's my link to access my server.
    static var baseURLString: URL { return URL(string: "http://localhost:8080/recipes")! }
    
    //Decoding the JSON Data. We're expecting a result that is an array or recipes, or an error.
    static func recipes(fromJSON data: Data) -> Result<[Recipe], Error> {
        //Try
        do {
            //Initiate a decoder.
            let decoder = JSONDecoder()
            //Date Formatter
            let dateFormatter = DateFormatter()
            dateFormatter.locale = Locale(identifier: "en_US_POSIX")
            dateFormatter.timeZone = TimeZone(secondsFromGMT: 0)
            dateFormatter.dateFormat = "yyyy-MM-dd"
            decoder.dateDecodingStrategy = .formatted(dateFormatter)
            //Create an arrayOfRecipes, that is created by trying to decode a Recipe object from the data we've recieved.
            let arrayOfRecipes = try decoder.decode([Recipe].self, from: data)
            //If we succeed, let's go ahead and return our arrayOfRecipes triumphantly.
            return .success(arrayOfRecipes)
        //If try fails
        } catch {
            //Return an error. Where does this error come from? I'm not quite sure.
            return .failure(error)
        }
    }
}

