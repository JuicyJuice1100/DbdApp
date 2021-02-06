import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MyBuildsPage } from './my-builds.page';

const routes: Routes = [
  {
    path: '',
    component: MyBuildsPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class MyBuildsPageRoutingModule {}
