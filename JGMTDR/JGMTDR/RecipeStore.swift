//
//  RecipeStore.swift
//  JGMTDR
//
//  Created by Payton Pehrson on 11/9/20.
//  Copyright © 2020 Payton Pehrson. All rights reserved.
//

import UIKit

class RecipeStore {
    var allRecipes = [Recipe]()
    
    //Creating a URLSession object
    private let session: URLSession = {
        let config = URLSessionConfiguration.default
        return URLSession(configuration: config)
    }()
    
    func fetchRecipes(completion: @escaping (Result<[Recipe], Error>) -> Void) {
        //Alright, let's get the path
        let url = RecipeAPI.baseURLString
        //And now we'll create a URLRequest
        let request = URLRequest(url: url)
        //And thus, we begin fetching with a lambda function taking data, response, and an error in.
        let task = session.dataTask(with: request) {
            (data, response, error) in
            //Use a function that will process our data into JSONData instead of strings.
            let result = self.processRecipeRequest(data: data, error: error)
            //Complete our asynchronous process
            OperationQueue.main.addOperation {
                completion(result)
            }
        }
        task.resume()
    }
    
    //Processing the jsonData returned from the fetch.
    private func processRecipeRequest(data: Data?, error: Error?) -> Result<[Recipe], Error> {
        //try to create a jsonData variable, if it can't return a failure.
        guard let jsonData = data else {
            return .failure(error!)
        }
        return RecipeAPI.recipes(fromJSON: jsonData)
    }
}
