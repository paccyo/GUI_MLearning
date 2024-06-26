
# 2024/06/04 BPS-sys ver1.0作成

import os
import pandas as pd

class ModelInfo:
    """
    モデル構造ファイル作成
    """
    def __init__(self):
        self.layers = ''
        self.imports = ''
        self.load_import_info()
    
    def load_import_info(self):
        """
        importテキスト読み込み
        """
        with open('packages/model_imports.txt') as f:
            imports_data = f.read()
        self.imports += imports_data + '\n\n'

    def send(self, model_dict, project_path, shape=None):
        """
        辞書からモデルを構築
        """
        self.generate_model(model_dict, project_path, shape)



    def generate_model(self, model_dict, project_path, shape=None):
        before_unique_layer_name = ''    # １つ前のレイヤー変数名(layername)
        first_unique_layer_name = ''     # 最初のレイヤー変数名(inputs)
        filal_unique_layer_name = ''     # 最後のレイヤー変数名(outputs)
        shape_flag = True
        for i, (unique_layer_name, layer_params) in enumerate(model_dict.items()):
            params = ''    # 各レイヤーパラメータの格納用変数
            if i == 0:
                first_unique_layer_name = unique_layer_name
            if i == len(model_dict)-1:
                filal_unique_layer_name = unique_layer_name
            
            # レイヤー関数名を取得
            layer_name = unique_layer_name[:-4]

            # パラメータ引数をセット
            for layer_param_name, layer_param_value in layer_params.items():
                if i == 0 and shape and shape_flag:
                    shape_flag = False
                    params += f'{layer_param_name}={shape}, '
                else:
                    params += f'{layer_param_name}={layer_param_value}, '
            
            # 不要なコンマを削除
            params = params[:-2]

            # 行ごとにレイヤー作成
            if before_unique_layer_name:
                self.layers += f'    {unique_layer_name} = {layer_name}({params})({before_unique_layer_name})\n'
            else:
                self.layers += f'    {unique_layer_name} = {layer_name}({params})\n'
            
            # １つ前のレイヤー名を更新
            before_unique_layer_name = unique_layer_name
            
        # 最終層作成
        self.layers += f'    model = Model(inputs={first_unique_layer_name}, outputs={filal_unique_layer_name})\n'

        self.write_modelfile(project_path)
        
    def write_modelfile(self, project_path):
        """
        モデルファイル書き出し
        """
        if self.layers:
            with open(f'{project_path}/model_info.py', 'w') as f:
                f.write(self.imports+'def model_build():\n'+self.layers+'    return model')

    def get_image_shape(self, image_size=(None, None), color_mode='rgb'):    
        if color_mode == 'rgb':
            color = 3
        else:
            color = 1
        return (image_size[0], image_size[1], color)
    
    def get_dataframe_shape(self, dataset_path):
        train_data_path = os.path.join(dataset_path, 'train_data.csv')
        df = pd.read_csv(train_data_path)
        return (len(df.values[0]),)

        
            

if __name__ == '__main__':
    # テストケース
    test_dic = {
        'Dense0000': {
            'units': 0,
            'use_bias': True,
            'kernel_initializer': '\'glorot_uniform\'',
            'bias_initializer': '\'zeros\'',
            'kernel_regularizer': None,
            'bias_regularizer': None,
            'activity_regularizer': None,
            'kernel_constraint': None,
            'bias_constraint': None,
            'lora_rank': None
        },

        'Activation0000': {
            'activation':None
        },

        'Conv2D0000': {
            'filters': 0,
            'kernel_size': (0, 0),
            'strides': (1, 1),
            'padding': '\'valid\'',
            'data_format': None,
            'dilation_rate': (1, 1),
            'groups': 1,
            'activation': None,
            'use_bias': True,
            'kernel_initializer': '\'glorot_uniform\'',
            'bias_initializer': '\'zeros\'',
            'kernel_regularizer': None,
            'bias_regularizer': None,
            'activity_regularizer': None,
            'kernel_constraint': None,
            'bias_constraint': None
        },

        'Conv1D0000': {
            'filters': 0,
            'kernel_size': 0,
            'strides': 1,
            'padding': '\'valid\'',
            'data_format': None,
            'dilation_rate': 1,
            'groups': 1,
            'activation': None,
            'use_bias': True,
            'kernel_initializer': '\'glorot_uniform\'',
            'bias_initializer': '\'zeros\'',
            'kernel_regularizer': None,
            'bias_regularizer': None,
            'activity_regularizer': None,
            'kernel_constraint': None,
            'bias_constraint': None
        },

        'MaxPooling2D0000': {
            'pool_size': (2, 2),
            'strides': None,
            'padding': '\'valid\'',
            'data_format': None,
            'name': None
        },

        'MaxPooling1D0000': {
            'pool_size': 2,
            'strides': None,
            'padding': '\'valid\'',
            'data_format': None,
            'name': None
        },

        'Flatten0000': {
            'data_format': None
        },

        'GlobalAveragePooling2D0000': {
            'data_format': None,
            'keepdims': False
        },


    }


    # 実行

    model_info = ModelInfo()
    model_info.send(test_dic)

    shape_size = model_info.get_shape(image_size=(256, 256), color_mode='rgb')
    print(shape_size)

