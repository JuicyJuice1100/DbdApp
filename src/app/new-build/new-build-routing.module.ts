import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { NewBuildPage } from './new-build.page';

const routes: Routes = [
  {
    path: '',
    component: NewBuildPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class NewBuildPageRoutingModule {}
