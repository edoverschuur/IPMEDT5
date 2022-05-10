<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;
use DB;

class DataTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        DB::table('data')->insert([
            'temperature' => 0,
            'humidity' => 0
        ]);
    }
}
