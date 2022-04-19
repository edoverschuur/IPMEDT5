<?php

namespace App\Http\Controllers;
use App\Models\Count;
use Illuminate\Http\Request;

class CountController extends Controller
{
    public function show(){
        return view('count.show')->with('count',Count::first()->amount);
    }
}
