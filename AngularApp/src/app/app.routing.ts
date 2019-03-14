import { RouterModule, Routes } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';
import { HomeComponent } from './home/home.component';
import { CatsComponent } from './cats/cats.component';
import { DogsComponent } from './dogs/dogs.component';
import { BirdsComponent } from './birds/birds.component';

const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'cats', component: CatsComponent },
    { path: 'dogs', component: DogsComponent },
    { path: 'birds', component: BirdsComponent }
];

export const routingModule: ModuleWithProviders = RouterModule.forRoot(routes);

